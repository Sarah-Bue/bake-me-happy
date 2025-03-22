// Toggle between viewing and editing user profile details
document.addEventListener("DOMContentLoaded", function() {
    const editProfileBtn = document.getElementById('edit-profile-btn');
    const cancelEditBtn = document.getElementById('cancel-edit-btn');
    const profileView = document.getElementById('profile-view');
    const profileEdit = document.getElementById('profile-edit');
    
    // Show edit form and hide view
    if (editProfileBtn) {
        editProfileBtn.addEventListener('click', function() {
            profileView.style.display = 'none';
            profileEdit.style.display = 'block';
        });
    }
    
    // Hide edit form and show view
    if (cancelEditBtn) {
        cancelEditBtn.addEventListener('click', function() {
            profileView.style.display = 'block';
            profileEdit.style.display = 'none';
        });
    }
});