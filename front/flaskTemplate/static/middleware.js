$('body').on('click', '.dropdown-item', function() {

	let theme = $(this).attr('themeValue');
	const fileInput = document.querySelector('#inputGroupFile01');

    if(document.querySelector('#inputGroupFile01').files.length == 0 ){
        document.getElementById("hashtagResult").innerHTML = 'No image provided!';
        $("#hashtag").show();
        $("#group1").hide();
        $("#group2").hide();
        $("#group3").hide();
    }
    else {

        var formData = new FormData();
        formData.append('fileInput', fileInput.files[0]);
        formData.append('themeValue', theme);

        $.ajax({
            type: 'POST',
            url: 'http://localhost:5000/image',
            data: formData,
            contentType: false,
            cache: false,
            processData: false,
            success: function (data) {
                document.getElementById("hashtagResult").innerHTML = data;
                $("#hashtag").show();
                $("#group1").hide();
                $("#group2").hide();
                $("#group3").hide();
            },
            error: function () {
                document.getElementById("hashtagResult").innerHTML = "There is a problem.<br>Please try again!";
                $("#hashtag").show();
                $("#group1").hide();
                $("#group2").hide();
                $("#group3").hide();
            }
        });

    }

});

$('body').on('click', '.btn.btn-primary', function() {
    document.getElementById("inputGroupFile01").value = '';
	$("#hashtag").hide();
	$("#group1").show();
	$("#group2").show();
	$("#group3").show();
});

