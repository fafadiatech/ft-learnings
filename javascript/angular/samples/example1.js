var app = angular.module('app', []);

app.controller('helloworld', function($scope){
	$scope.message = "Hello World!";
	$scope.first = 1;
	$scope.second = 999;

	$scope.updateValue = function(){
		$scope.result = $scope.first + $scope.second;
	}

	$scope.names = ['Sidharth', 'Khyati', 'Dilip', 'Jayshree', 'Manan', 'Vyoma'];
});