$('body').on('click', '.dropdown-item', function() {

	let theme = $(this).attr('themeValue');
	const fileInput = document.querySelector('#inputGroupFile01');

	var formData = new FormData();
    formData.append('fileInput', fileInput.files[0]);
    formData.append('themeValue', theme);

    $.ajax({
        type: 'POST',
        url: '/route',
        data: formData,
        contentType: false,
        cache: false,
        processData: false,
        success: function (data) {
            document.getElementById("hashtagResult").innerHTML = "#sportwear #sportlife #sporty #sportshoes #sportsgirl #sportstyle #sportmotivation #athletics #sportfashion #sportslife #body #shape #bodygoals #positivevibes #gainmuscles #sportlife #bodypositive #bodylove #loveyourself #training #strong #sportmotivation #fit #musclegain #motivate #workout #teamshape ";
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

});

$('body').on('click', '.btn.btn-primary', function() {
	$("#hashtag").hide();
	$("#group1").show();
	$("#group2").show();
	$("#group3").show();
});

