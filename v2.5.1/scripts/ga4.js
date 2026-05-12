(function() {
  // Niet tracken op localhost
  if (location.hostname === 'localhost' || location.hostname === '127.0.0.1') {
    return;
  }

  var script = document.createElement('script');
  script.async = true;
  script.src = 'https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX';
  document.head.appendChild(script);

  window.dataLayer = window.dataLayer || [];
  function gtag(){ dataLayer.push(arguments); }
  window.gtag = gtag;
  gtag('js', new Date());
  gtag('config', 'G-2RLMHTLGRH');
})();