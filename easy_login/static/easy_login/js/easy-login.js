function ToggleEasyLoginMenu() {
    var toggleClassNames = ['easy-login-detail-info', 'easy-login-toggle'];
    toggleClassNames.forEach(function (className, index) {
        var elements = document.getElementsByClassName(className);
        for (var i = 0, l = elements.length; i < l; i++) {
            var obj = elements[i];
            if (obj.style.display === "none") {
                obj.style.display = "";
            } else {
                obj.style.display = "none";
            }
        }
        });
}


document.getElementById('id_user_name').onchange = function() {
    document.getElementById('easy-login-form').submit();
};
