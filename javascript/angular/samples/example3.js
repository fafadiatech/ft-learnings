var app = angular.module('app', []);

app.controller('GroceryCtrl', function($scope){
	$scope.groceries = [
		{name: "Snakker", purchased: false},
		{name: "Oreo", purchased: false},
		{name: "Snickers", purchased: false},
	];

	$scope.getList = function(){
		return $scope.showList ? "ul.html" : "ol.html";
	}
});

