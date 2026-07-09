if ("serviceWorker" in navigator) {
    navigator.serviceWorker.register("/static/serviceworker.js")
        .then(() => {
            console.log("Service Worker registered");
        })
        .catch(error => {
            console.log("Service Worker registration failed:", error)
        });
}
