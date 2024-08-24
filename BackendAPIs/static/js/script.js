document.addEventListener("DOMContentLoaded", function () {
    // Populate subject dropdown based on selected category
    const categoryRadios = document.querySelectorAll('input[name="category"]');
    const subjectSelect = document.getElementById("subject");
  
    function populateSubjectOptions() {
        const selectedCategory = document.querySelector('input[name="category"]:checked').value;
        subjectSelect.innerHTML = ""; // Clear existing options
  
        const options = selectedCategory === "Software" 
            ? ["Antivirus", "Office Suite", "Development Tools"] 
            : ["Monitor", "Keyboard", "Mouse", "Printer"];
  
        options.forEach(option => {
            const newOption = document.createElement("option");
            newOption.value = option;
            newOption.text = option;
            subjectSelect.add(newOption);
        });
    }
  
    categoryRadios.forEach(radio => radio.addEventListener("change", populateSubjectOptions));
  
    // Initial population based on the default selected radio
    populateSubjectOptions();
  
    // Handle form submission
    const requestForm = document.getElementById("requestForm");
    const submissionMessage = document.getElementById("submissionMessage");
    const formContainer = document.querySelector(".form-container");
  
    requestForm.addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent default form submission
  
        // Hide the form and display the success message
        formContainer.classList.add("hidden");
        submissionMessage.classList.remove("hidden");
    });
  
    // Handle 'Back to Dashboard' link
    const backToDashboard = document.getElementById("backToDashboard");
    backToDashboard.addEventListener("click", function (event) {
        event.preventDefault();
        // Reset the form and navigate back to dashboard (for this example, just reload the page)
        formContainer.classList.remove("hidden");
        submissionMessage.classList.add("hidden");
        requestForm.reset();
        populateSubjectOptions(); // Reset the dropdown options
    });
  });