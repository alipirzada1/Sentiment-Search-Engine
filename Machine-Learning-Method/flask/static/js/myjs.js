$('document').ready(function() {

	// ========================================
	// INDEX PAGE
	// ========================================
	
	$('.aboutPage').click(function() {
		location.href = "{{ url_for('about') }}";
	});

	$('#Politics').hide();
	$('#Sport').hide();
	$('#Vehicles').hide();

	$('#btnTech').click(function() {
		$('*').removeClass('active');
		$(this).addClass('active');

		$('#Vehicles, #Sport, #Politics').hide();
		$('#Tech').show();
	});

	$('#btnPolitics').click(function() {
		$('*').removeClass('active');
		$(this).addClass('active');

		$('#Sport , #Tech , #Vehicles').hide();
		$('#Politics').show();
	});

	$('#btnSport').click(function() {
		$('*').removeClass('active');
		$(this).addClass('active');

		$('#Tech , #Politics , #Vehicles').hide();
		$('#Sport').show();
	});

	$('#btnVehicles').click(function() {
		$('*').removeClass('active');
		$(this).addClass('active');

		$('#Politics , #Sport , #Tech').hide();
		$('#Vehicles').show();
	});
});