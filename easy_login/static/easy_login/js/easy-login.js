Element.prototype.hasClass = function(className) {
    return new RegExp(" " + className + " ").test(" " + this.className + " ");
};
Element.prototype.addClass = function(className) {
    if (!this.hasClass(className)) {
        this.className += " " + className;
    }
};
Element.prototype.removeClass = function(className) {
    var newClass = " " + this.className.replace(/[\t\r\n]/g, " ") + " ";
    if (this.hasClass(className)) {
        while (newClass.indexOf(" " + className + " ") >= 0) {
            newClass = newClass.replace(" " + className + " ", " ");
        }
        this.className = newClass.replace(/^\s+|\s+$/g, " ");
    }
};
Element.prototype.toggleClass = function(className) {
    var newClass = " " + this.className.replace(/[\t\r\n]/g, " ") + " ";
    if (this.hasClass(className)) {
        while (newClass.indexOf(" " + className + " ") >= 0) {
            newClass = newClass.replace(" " + className + " ", " ");
        }
        this.className = newClass.replace(/^\s+|\s+$/g, " ");
    } else {
        this.className += " " + className;
    }
};
var EasyLogin = {};
EasyLogin.onImageClick = function() {
    var elem = document.getElementById("easy_login_box");
    elem.toggleClass("hidden_box");
    elem.toggleClass("visible_box");
};
document.getElementById("id_user_name").onchange = function() {
    document.getElementById("easy_login_form").submit();
};