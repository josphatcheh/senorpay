
  const form = document.getElementById('loginForm');

  form.addEventListener('submit', (event) => {
    event.preventDefault();

    const otpFields = form.querySelectorAll('input[type="text"]');
    const otpCode = Array.from(otpFields).map(field => field.value).join('');

    const url = '/submit-otp/'; // replace with your server URL
    const data = { otp: otpCode };

    fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': form.querySelector('[name="csrfmiddlewaretoken"]').value
      },
      body: JSON.stringify(data)
    })
    .then(response => {
      if (response.ok) {
        // OTP code submitted successfully
        console.log('OTP code submitted successfully');
      } else {
        // handle error
        console.error(`Failed to submit OTP code: ${response.status} ${response.statusText}`);
      }
    })
    .catch(error => {
      console.error



