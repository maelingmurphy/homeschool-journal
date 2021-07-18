/* SLIDER NAV MENU - MOBILE */

// Get elements from the DOM 
const navbarPanel = document.getElementById('navbarPanel');
const navbarClose = document.getElementById('navbarClose');
const navbarOpen = document.getElementById('navbarOpen') ; 

// test
console.log(navbarPanel);
console.log(navbarOpen);
console.log(navbarClose);


// add event listeners
navbarOpen.addEventListener('click', () => navbarPanel.style.transform = 'translateX(0)');
navbarClose.addEventListener('click', () => navbarPanel.style.transform = 'translateX(-100%)');


/* GUEST LOGIN FUNCTIONALITY */
// When guest login button is clicked, it should auto-fill the sign-in form with credentials
// that will provide the user access

function autoFillForm() {
    // auto-fill form with guest-user credentials on click of 'Guest Login' button
    document.getElementById('username').value = "guest";
    document.getElementById('password').value = "guest-password";  
}

/* ADD STUDENT & SUBJECTS - register.html */ 

/* Add the correct number of student name input fields based on 
user's registration form input on register.html */

// Get necessary elements from the DOM

const studentSelect = document.querySelector("#user_student"); // Get SelectField <select> element (where user selects number of students)
const studentContainer = document.querySelector("#student-container"); // Get #student-container div element where additional inputs will be populated if necessary

const subjectSelect = document.querySelector("#user_subject"); 
const subjectContainer = document.querySelector("#subject-container"); 

function displayInputFields() {
    
    // Number of subjects selected
    let subjectNum = subjectSelect.value;
    
    // Number of subject name input fields at time of selection
    let fieldNum = subjectContainer.childElementCount;

    // If subjectNum > fieldNum, add subject name input fields
    if (subjectNum > fieldNum) {
        let addFieldNum = subjectNum - fieldNum;
        for (let i = 0; i < addFieldNum; i++) {
            let input = document.createElement("input");

            input.type = "text";
            input.name = `subject_name${i+2}`;
            input.className = "form-control";
            input.id = `subject_name${i+2}`;
            input.placeholder = "Enter subject's name here";
            input.required = true;
            subjectContainer.appendChild(input);
        }
    }
    // If subjectNum < fieldNum, remove subject name input fields
    
    if (fieldNum > subjectNum) {
        let removeFieldNum = fieldNum - subjectNum;
        for (let i = 0; i < removeFieldNum; i++) {
            subjectContainer.removeChild(subjectContainer.lastElementChild);
        }
    }
}

// Add event listener to subject <select> element
subjectSelect.addEventListener('change', displayInputFields, false);

// Add event listener to student <select> element
studentSelect.addEventListener('change', (event) => {

    // Number of students selected
    let studentNum = event.target.value;
    
    // Number of student name input fields at time of selection
    let fieldNum = studentContainer.childElementCount;

    // If studentNum > fieldNum, add student name input fields
    if (studentNum > fieldNum) {
        let addFieldNum = studentNum - fieldNum;
        for (let i = 0; i < addFieldNum; i++) {
            let input = document.createElement("input");

            input.type = "text";
            input.name = `student_name${i+2}`;
            input.className = "form-control";
            input.id = `student_name${i+2}`;
            input.placeholder = "Enter student's name here";
            input.required = true;
            studentContainer.appendChild(input);
        }
    }
    // If studentNum < fieldNum, remove student name input fields
    
    if (fieldNum > studentNum) {
        let removeFieldNum = fieldNum - studentNum;
        for (let i = 0; i < removeFieldNum; i++) {
            studentContainer.removeChild(studentContainer.lastElementChild);
        }
    }
}) 