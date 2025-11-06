document.addEventListener('DOMContentLoaded', function () {
    
    const fileInput = document.getElementById('imageInput');
    const previewWrapper = document.getElementById('imagePreview');
    const previewImg = document.getElementById('previewImg');
    const resultDiv = document.getElementById('prediction');
    const form = document.querySelector('form');
    const submitBtn = document.getElementById('submitBtn');

    // allowed file types and max file size
    const MAX_BYTES = 5 * 1024 * 1024; // 5 MB
    const ALLOWED_TYPES = ['image/jpeg', 'image/png', 'image/gif', 'image/webp'];

    //show a message in the result area
    function showMessage(message, isError) {
        resultDiv.textContent = message;
        resultDiv.style.color = isError ? '#7a1f1f' : '#0b3b5c';
    }

    // Reset preview and messages
    function resetPreview() {
        previewImg.src = '';
        previewWrapper.style.display = 'none';
        previewImg.removeAttribute('alt');
    }

    // Validate file type and size.
    function validateFile(file) {
        if (!file) return 'No file selected.';
        if (!ALLOWED_TYPES.includes(file.type)) return 'Unsupported file type. Please upload PNG, JPG, GIF, or WEBP.';
        if (file.size > MAX_BYTES) return 'File is too large. Please select a file smaller than 5 MB.';
        return null;
    }

    fileInput.addEventListener('change', function () {
        const file = this.files && this.files[0];

        showMessage('');
        resetPreview();

        // Basic validation
        const error = validateFile(file);
        if (error) {
            showMessage(error, true);
            return;
        }

        // Read the file as a data URL and display it in the preview image
        const reader = new FileReader();
        reader.onload = function (e) {
            previewImg.src = e.target.result;
            previewImg.alt = file.name || 'Selected image';
            previewWrapper.style.display = 'block';
            previewWrapper.setAttribute('aria-hidden', 'false');
        };
        reader.onerror = function () {
            showMessage('Unable to read the selected file. Please try another image.', true);
        };
        reader.readAsDataURL(file);
    });

    form.addEventListener('submit', function () {

        if (submitBtn) {
            submitBtn.disabled = true;
            submitBtn.textContent = 'Predicting... Please wait';
        }
        showMessage('Predicting... Please wait', false);
    });

    if (!fileInput.value) resetPreview();
});
