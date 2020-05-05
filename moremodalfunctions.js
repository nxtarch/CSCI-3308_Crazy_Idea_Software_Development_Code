function openModal() {

    var myInput = document.getElementById("psw");
    var confirmMyInput = document.getElementById("cpsw");
	  var letter = document.getElementById("letter");
	  var capital = document.getElementById("capital");
	  var number = document.getElementById("number");
	  var length = document.getElementById("length");
    var match = document.getElementById("match");
    // var fisrt = document.getElementById("first");
    // var last = document.getElementById("last");
    // var user = document.getElementById("user");


	// When the user starts to type something inside the password field
	myInput.onkeyup = function() {
       console.log('helllooo')


        var lowerCaseLetters = /[a-z]/g;
        var upperCaseLetters = /[A-Z]/g;
        var numbers = /[0-9]/g;
        var minLength = 8;




        //  lowercase letters
        if(myInput.value.match(lowerCaseLetters)) {
            letter.classList.remove("invalid");
            letter.classList.add("valid");
        } else {
            letter.classList.remove("valid");
            letter.classList.add("invalid");
        }

        //  capital letters
        if(myInput.value.match(upperCaseLetters)) {
            capital.classList.remove("invalid");
            capital.classList.add("valid");
        } else {
            capital.classList.remove("valid");
            capital.classList.add("invalid");
        }

        //  numbers
        if(myInput.value.match(numbers)) {
            number.classList.remove("invalid");
            number.classList.add("valid");
        } else {
            number.classList.remove("valid");
            number.classList.add("invalid");
        }

        //  length
        if(myInput.value.length >= minLength) {
            length.classList.remove("invalid");
            length.classList.add("valid");
        } else {
            length.classList.remove("valid");
            length.classList.add("invalid");
        }




    }


    confirmMyInput.onkeyup = function() {
                // Validate password and confirmPassword
                var passEqualsConfPass = (false);
                if (myInput.value == confirmMyInput.value)
                {
                  passEqualsConfPass = (true);
                }
                else
                {
                  passEqualsConfPass = (false);
                }


                if(passEqualsConfPass == (true)) {
                    match.classList.remove("invalid");
                    match.classList.add("valid");
                } else {
                    match.classList.remove("valid");
                    match.classList.add("invalid");
                }

                enableButton(letter, capital, number, length, match);
    }
}


function enableButton(letter, capital, number, length, match) {

    var button = document.getElementById('my_submit_button');
    var condition = (false);
    if(letter.classList == "valid"&&number.classList == "valid"&&capital.classList == "valid"&&match.classList == "valid")
    {
      condition = (true);
    }
    else
    {
      condition = (false);
    }
    if(condition == (true)) {
            button.disabled = false;
        }
    else {
      button.disabled = true;
    }
    }

function onClickFunction() {
    alert("You have successfully created an account with us.")
    $('#myModal').modal('hide');
    login();
}


//help functions to enable/disable forms and buttons
function enable(buttonId)
{
  var button = document.getElementById(buttonId);
  button.disabled = false;
}

function disable(buttonId)
{
  var button = document.getElementById(buttonId);
  button.disabled = true;
}


//TO DO: add form input for the following functions
//       also add proper DB communication elements



//keeps track of if the user is logged in or not
var loggedin = false;

//called whene login/logout button is clicked
function loginClick()
{
  if(!loggedin)
  {//opens login modal if user not logged in
    $('#loginModal').modal('show');
  }
  else
  {//otherwise marks user as not logged in
    //enables signup button and changes log out button to login
    loggedin=false;
    var button = document.getElementById("loginModalButton");
    button.innerHTML="login";
    enable("signupModalButton");
  }
}



//called when login button on loginModal is clicked
function login()
{
      disable("signupModalButton");

      //call verify login info funtion here

      $('#loginModal').modal('hide');
      var button = document.getElementById("loginModalButton");
      button.innerHTML="log out";
      loggedin=true;
}


//the following are functions for the buttons on the profile page
function changeUserName()
{
  disable("changeUsernamebtn");
  enable("newUsernameForm");
  enable("confirmUsernameForm");
  //implement form stuff here, or maybe in save function
  enable("saveUsernamebtn");
}

function saveUserName()
{
  disable("saveUsernamebtn");
  disable("newUsernameForm");
  disable("confirmUsernameForm");
  //veryify new user name here
  //change DB info of verification works
  enable("changeUsernamebtn");
}

function changePSW()
{
  disable("changePSWbtn");
  enable("currPswForm");
  enable("newPswForm");
  enable("confirmPswForm");
//implement form stuff here, or maybe in save function
  enable("savePSWbtn");
}

function savePSW()
{
  disable("savePSWbtn");
  disable("currPswForm");
  disable("newPswForm");
  disable("confirmPswForm");
  //veryify password here
  //change DB info of verification works
  enable("changePSWbtn");
}

//do same stuff for next stuff
function changePrefs()
{
  disable("changePreferencesbtn");
  var dairy = document.getElementById("dairyBox");
  var nuts = document.getElementById("nutsBox");
  var seafood = document.getElementById("seafoodBox");
  var gluten = document.getElementById("glutenBox");
  var soy = document.getElementById("soyBox");
  var vegetarian = document.getElementById("vegetarianBox");
  var vegan = document.getElementById("veganBox");
  var kosher = document.getElementById("kosherBox");

  dairy.disabled=false;
  nuts.disabled=false;
  seafood.disabled=false;
  gluten.disabled=false;
  soy.disabled=false;
  vegetarian.disabled=false;
  vegan.disabled=false;
  kosher.disabled=false;

  enable("savePreferencesbtn");
}

function savePrefs()
{
  disable("savePreferencesbtn");

  var dairy = document.getElementById("dairyBox");
  var nuts = document.getElementById("nutsBox");
  var seafood = document.getElementById("seafoodBox");
  var gluten = document.getElementById("glutenBox");
  var soy = document.getElementById("soyBox");
  var vegetarian = document.getElementById("vegetarianBox");
  var vegan = document.getElementById("veganBox");
  var kosher = document.getElementById("kosherBox");

  dairy.disabled=true;
  nuts.disabled=true;
  seafood.disabled=true;
  gluten.disabled=true;
  soy.disabled=true;
  vegetarian.disabled=true;
  vegan.disabled=true;
  kosher.disabled=true;

  enable("changePreferencesbtn");

}
