// Add the correct number of student name input fields based on user's registration form input on register.html

// Get necessary elements from the DOM

const studentSelect = document.querySelector("#user_student"); // Get SelectField <select> element (where user selects number of students)
const studentContainer = document.querySelector("#student-container"); // Get #student-container div element where additional inputs will be populated if necessary

// Add event listener to <select> element
studentSelect.addEventListener('change', (event) => {

    // Number of students selected
    var studentNum = event.target.value;
    
    // Number of student name input fields at time of selection
    var fieldNum = studentContainer.childElementCount;

    // If studentNum > fieldNum, add student name input fields
    if (studentNum > fieldNum) {
        var addFieldNum = studentNum - fieldNum;
        for (i = 0; i < addFieldNum; i++) {
            var input = document.createElement("input");

            input.type = "text";
            input.name = `student_name${i+2}`;
            input.className = "form-control";
            input.id = `student_name${i+2}`;
            input.placeholder = "Enter student's name here"
            studentContainer.appendChild(input);
        }
    }
    // If studentNum < fieldNum, remove student name input fields
    
    if (fieldNum > studentNum) {
        var removeFieldNum = fieldNum - studentNum;
        for (i = 0; i < removeFieldNum; i++) {
            studentContainer.removeChild(studentContainer.lastElementChild);
        }
    }
    
})

