function IndexController($scope, $http) {
    $http.get('/api/v1/image/?format=json').
        success(function(images){
//            console.log(images);
            $scope.images = images.objects;
            catRandomTransformation();
        });

    $scope.onCatClick = function(element) {
        console.log("STOP CLICKING THE DUMB CAT");
        catRandomTransformation();
    };

    function catRandomTransformation(){
        $scope.image = $scope.images[Math.floor(Math.random() * $scope.images.length)];

    }

    $scope.onPostClick = function(element) {
        console.log("STOP CLICKING THE DUMB POST");
        postRandomTransformation();
    };

    function postRandomTransformation(){
        $http.get('/fbpost').
        success(function(fbPostToDisplay){
            console.log(fbPostToDisplay)
            $scope.post = fbPostToDisplay.friend_posts.story;
            console.log(fbPostToDisplay.friend_posts.story);
        });
    }

    postRandomTransformation();

// -------get function to call /fbpost/
//    function fbPostToDisplay(){
//        $http.get('/api/v1/image/?format=json').
//
//    }

}

// "you're not REMOVING the cat, you're CHANGING the cat." - AngularJS, two-way binding
// Backburner Issues:
//      - Need to next enter a score into the database




//Facebook:
//    - Two routes:
//        1. Make an api call to server, since it knows the user, get their fb info on the server,
//              uses a python library and gets a post, and returns to angular to display
// Make an api call to server


//        2. Second way is to just use Angular to call to fb, and your Angular code would have access to everything and just shows a post.