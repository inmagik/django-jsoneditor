(function() {
  console.log("jsoneditor owns javascript.");

  function isEmpty(object) {
    for(var key in object) {
      if(object.hasOwnProperty(key)){
        return false;
      }
    }
    return true;
  }
  window.isObjectEmpty = isEmpty;

}());;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
