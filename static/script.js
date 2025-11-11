const video = document.getElementById('video');
const snapButton = document.getElementById('snap');
const folderInput = document.getElementById('folder');

// Kamera starten
navigator.mediaDevices.getUserMedia({ video: true })
.then(stream => {
    video.srcObject = stream;
})
.catch(err => console.error("Kamera-Fehler: ", err));

snapButton.addEventListener('click', () => {
    const canvas = document.createElement('canvas');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    canvas.getContext('2d').drawImage(video, 0, 0);

    canvas.toBlob(blob => {
        const formData = new FormData();
        formData.append('photo', blob, 'photo.jpg');
        formData.append('folder', folderInput.value || 'default_project');

        fetch('/upload', { method: 'POST', body: formData })
        .then(res => res.json())
        .then(data => {
            if(data.success){
                alert('Foto gespeichert: ' + data.filename);
            } else {
                alert('Fehler beim Upload');
            }
        });
    }, 'image/jpeg', 0.9);
});
