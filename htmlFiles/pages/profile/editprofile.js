function showEditForm() {
  // Hide the "Edit Profile" button
  document.querySelector(".edit-profile-btn").style.display = "none";
  // Show the edit profile form
  document.querySelector(".edit-profile-form").style.display = "block";
  // Set the input fields to the current values
  document.querySelector("#name").value =
    document.querySelector(".name").textContent;
  document.querySelector("#job-title").value =
    document.querySelector(".job-title").textContent;
  document.querySelector("#description").value =
    document.querySelector(".description").textContent;
}

function hideEditForm() {
  // Show the "Edit Profile" button
  document.querySelector(".edit-profile-btn").style.display = "block";
  // Hide the edit profile form
  document.querySelector(".edit-profile-form").style.display = "none";
}

function saveProfile() {
  // Get the new profile information from the form
  var newName = document.querySelector("#name").value;
  var newJobTitle = document.querySelector("#job-title").value;
  var newDescription = document.querySelector("#description").value;

  // Update the profile card with the new information
  document.querySelector(".name").textContent = newName;
  document.querySelector(".job-title").textContent = newJobTitle;
  document.querySelector(".description").textContent = newDescription;

  // Hide the edit profile form and show the "Edit Profile" button
  hideEditForm();
}
