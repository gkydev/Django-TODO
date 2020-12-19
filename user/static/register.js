const regForm = document.querySelector('#regForm');
const username = document.querySelector('#username');
const email = document.querySelector('#email');
const password = document.querySelector('#password');
const password2 = document.querySelector('#password2');

/**
 * checks input to makes sure it has value
 * @param {string} input 
   @param {string} message 
 */
function showError( input, message)
{
  const formControl = input.parentElement;
  formControl.className = 'form-control error';

  const small = formControl.querySelector('small');
  small.textContent = message;
}

function removeError( input ){
  const formControl = input.parentElement;
  formControl.className = 'form-control error';
}


/**
 * 
 * @param {array} inputs 
 */
function validateInputs( inputs )
{
  let invalids = [];
  inputs.forEach(function( input )
  {
    if( input.value.trim() === "" )
    {
      invalids.push( input );
      //passes in the label's text content as the message
      showError( input, `${input.previousElementSibling.textContent} is required`)
    }
  });
  
  if( invalids.length > 0 )
  {
    return false;

  }

}


/**
 * checks email to see if it's valid
 * @param {string} email 
 */
function validEmail( email )
{
    const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    // return re.test(String(email).toLowerCase());
    if( !re.test( email.value.trim() ) )
    {
      showError( email, 'Email is not valid');
      
    }
}


function checkLength( input, min, max )
{
  if( input.value.length < min )
  {
    showError( input, `${ fieldName( input ) } must be at least ${ min } characters`)
  }
  if( input.value.length > max )
  {
    showError( input, `${ fieldName( input ) } must be less than ${ max } characters`)
  }
}

function checkPasswords( pass1, pass2 )
{
  if( pass1 != pass2 )
  {
    showError( pass1, `Passwords must match`)
    showError( pass2, `Passwords must match`)
  }
}



/**
 * 
 * @param {sting} input 
 */
function fieldName( input )
{
  return input.id.charAt( 0 ).toUpperCase() + input.id.slice( 1 );
};



regForm.addEventListener('submit', function(e)
{
  e.preventDefault();
  
  validateInputs( [username, email, password, password2] );
  checkPasswords( password, password2 )
  checkLength( username, 3, 20);
  checkLength( password, 3, 20);
  checkLength( password2, 3, 20);
  validEmail( email );
  
});