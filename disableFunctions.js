document.oncontextmenu = function () {
  return false;
  }
window.addEventListener('mousewheel', function(event){
  if (event.ctrlKey === true || event.metaKey) {
    event.preventDefault();
  }
  },{ passive: false});

//firefox
window.addEventListener('DOMMouseScroll', function(event){
    if (event.ctrlKey === true || event.metaKey) {
        event.preventDefault();
    }
  },{ passive: false});
document.addEventListener('DOMContentLoaded', function (event) {
  document.body.style.zoom = 'reset';
  document.addEventListener('keydown', function (event) {
    if ((event.ctrlKey === true || event.metaKey === true)
    && (event.which === 61 || event.which === 107
      || event.which === 173 || event.which === 109
      || event.which === 187  || event.which === 189))
      {
        event.preventDefault();
      }
  }, false);
  document.addEventListener('mousewheel DOMMouseScroll', function (event) {
    if (event.ctrlKey === true || event.metaKey) {
      event.preventDefault();
    }
  }, false);
}, false);