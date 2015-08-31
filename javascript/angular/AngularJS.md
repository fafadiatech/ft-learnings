
[AngularJS Tutorial](https://docs.angularjs.org/tutorial)
====================

1. In Angular view is projection of model through template. Which mean any time underlying models change, it refreshes the appropriate binding points which updates the view.
2. **ng-app** attribute (which is implemented as ngApp directive. **NOTE:** In angular spinal-case are used for custom attributes and camelCase for directive that implement those custom attributes) allows us to figure out which part of page is angular application.
3. Using ng-app we can either make entire HTML page as Angular application or fragments of HTML page as angular application
4. Binding are denoted by `{{}}` double curly braces


```html
<html ng-app="phonecatApp">
<head>
  ...
  <script src="bower_components/angular/angular.js"></script>
  <script src="js/controllers.js"></script>
</head>
<body ng-controller="PhoneListCtrl">

  <ul>
    <li ng-repeat="phone in phones">
      <span>{{phone.name}}</span>
      <p>{{phone.snippet}}</p>
    </li>
  </ul>

</body>
</html>
```

```javascript
var phonecatApp = angular.module('phonecatApp', []);

phonecatApp.controller('PhoneListCtrl', function ($scope) {
  $scope.phones = [
    {'name': 'Nexus S',
     'snippet': 'Fast just got faster with Nexus S.'},
    {'name': 'Motorola XOOM™ with Wi-Fi',
     'snippet': 'The Next, Next Generation tablet.'},
    {'name': 'MOTOROLA XOOM™',
     'snippet': 'The Next, Next Generation tablet.'}
  ];
});
```
5. In the listing above: We've attached ng-controller directive to PhoneListCtrl **controller** to body tag. 
6. ng-repeat expression can be used iterate over model phones defined in our controller. This will allow us to get rid of any hard-coding that we might have in our HTML
7. **Scope** is an important concept in Angular, it is the glue that gets controller, models and templates working. It allows isolation and sync at the same time. Any changes to models are reflected on views/templates, any changes that happen on views are reflected on models
8. Angular developers prefer working with [Jasmine](http://jasmine.github.io/) which is a BDD tool, [Karma runner](http://karma-runner.github.io/0.13/index.html) can be configured to run with appropriate plugins to run angular tests. All this is possible becase we've separated out controllers and views using Angular.

```html
<div class="container-fluid">
  <div class="row">
    <div class="col-md-2">
      <!--Sidebar content-->

      Search: <input ng-model="query">

    </div>
    <div class="col-md-10">
      <!--Body content-->

      <ul class="phones">
        <li ng-repeat="phone in phones | filter:query">
          {{phone.name}}
          <p>{{phone.snippet}}</p>
        </li>
      </ul>

    </div>
  </div>
</div>
```
9. filter function can be used with data binding, note how the ng-model directive is used and chained with ng-repeat
10. [Protractor](https://github.com/angular/protractor) is a tool that is used to perform E2E tests for Angular. It complements Jasmine
11. Continue from [here](https://docs.angularjs.org/tutorial/step_04)