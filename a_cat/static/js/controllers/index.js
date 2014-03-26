function IndexController($scope, $http) {
    $http.get('/api/v1/image/?format=json').
        success(function(images){
//            console.log(images);
            $scope.images = images.objects;
            catRandomTransformation();
        });

    $scope.onCatClick = function(element) { // TODO connect this to DB
        console.log("STOP CLICKING THE DUMB CAT");
        catRandomTransformation();
        postRandomTransformation(); //this is here so both the cat and the post refresh. Logic: so people don't just click the post to see more cats
    };

    function catRandomTransformation(){
        $scope.image = $scope.images[Math.floor(Math.random() * $scope.images.length)];

    }

    $scope.onPostClick = function(element) {
        console.log("STOP CLICKING THE DUMB POST");
        postRandomTransformation();
        catRandomTransformation(); //this is here so both the cat and the post refresh. Logic: so people don't just click the post to see more cats
    };

    function postRandomTransformation(){
        $http.get('/fbpost').
        success(function(fbPostToDisplay){
            console.log(fbPostToDisplay)
            $scope.post = fbPostToDisplay.friend_posts.story;
            $scope.picture = fbPostToDisplay.picture;
            $scope.name = fbPostToDisplay.name;
            console.log(fbPostToDisplay.friend_posts.story);
        });
    }

    postRandomTransformation();


}

//Connect to database