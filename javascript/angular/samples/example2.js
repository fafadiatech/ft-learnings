var app = angular.module('app', []);

app.controller('RandNumberGenerator1Ctrl', function($scope){
	$scope.randomNum = Math.floor((Math.random() * 10) + 1);
});

app.controller('RandNumberGenerator2Ctrl', function($scope){
	$scope.randomNum = Math.floor((Math.random() * 10) + 1);
});