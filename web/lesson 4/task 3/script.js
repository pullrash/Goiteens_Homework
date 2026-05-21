document.getElementById('file-input').addEventListener('change', function(event) {
    const file = event.target.files[0];
    if (!file) return;

    const reader = new FileReader();

    reader.onload = function(e) {
        const content = e.target.result;
        const lines = content.split(/\r?\n/); 
        
        const container = document.getElementById('playlist-container');
        container.innerHTML = ''; 

        lines.forEach(line => {
            const trimmedLine = line.trim();
            
            if (trimmedLine !== '' && trimmedLine.includes(' - ')) {
                const [artist, songTitle] = trimmedLine.split(' - ');

                const songElement = document.createElement('div');
                songElement.className = 'song-item';
                songElement.innerHTML = `<strong>${artist.trim()}</strong> — ${songTitle.trim()}`;
                
                container.appendChild(songElement);
            }
        });
    };

    reader.readAsText(file, 'UTF-8');
});