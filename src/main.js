import emailjs from 'emailjs-com'
let apiKey= "hfge1I3G7K-7HSa14"
const sendEmail = e => {
    e.preventDefault()

    emailjs
    .sendForm('gmail', apiKey, e.target, "hfge1I3G7K-7HSa14")
    .then(
      result => {
        console.log(result.text)
      },
      error => {
        console.log(error.text)
      }
    )
}
const form = document.getElementById('form')
form.addEventListener('submit',sendEmail)