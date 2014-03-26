var a_cat = angular.module('a_cat', ['ngRoute']);

a_cat.config(['$routeProvider', function($routeProvider) {
    $routeProvider.
        when('/', { templateUrl: '/static/views/index.html', controller: IndexController}).
        when('/blog', { templateUrl: '/static/views/blog.html' }).

        otherwise({redirectTo: '/'});

}]);


// This Page:

// indexController isn't referring to a file name, it is referring to the function name
// housed in the appropriate file inside of js/controllers/ <- currently this is empty

// UNCLEAR on what $routeProvider is