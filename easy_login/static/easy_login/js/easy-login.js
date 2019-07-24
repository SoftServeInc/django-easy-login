$(document).ready(function(){
    $(".easy-login-flex-1").click(function(){
        $(".easy-login-flex-2").fadeToggle("slow");
        $(".easy-login-flex-3").fadeToggle("slow");
    });

    $('#id_user_name').on('change', function() {
         $("#easy-login-form" ).submit();
    });
});
