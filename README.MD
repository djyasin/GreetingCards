
# Greetery Cards API ReadMe

An API to store data for a custom greeting card interface.

Endpoints:
An API to store data for a custom greeting card interface.

Endpoints:
BaseURL	                                URL	Input	            Output
https://greeterycards.herokuapp.com/	/ecard/user_list		List of All Users
https://greeterycards.herokuapp.com/	/ecard/user_detail/<id>/	user by id	User Info and List of All Users You Follow
https://greeterycards.herokuapp.com/	/cards/	-	list of cards from users you follow
https://greeterycards.herokuapp.com/	/cards/me/	-	list of cards you have made
https://greeterycards.herokuapp.com/	/ecard/create	card data	new card
https://greeterycards.herokuapp.com/	/ecard/new_user		Create User
https://greeterycards.herokuapp.com/	/ecard/edit/<id>/	card data	Edit/Update Card
https://greeterycards.herokuapp.com/	/ecard/card_list		List of All Cards
https://greeterycards.herokuapp.com/	/ecard/card_detail/<id>/	-	Data for Card with Specific ID
https://greeterycards.herokuapp.com/	/ecard/delete_card/<id>	-	Delete Card
https://greeterycards.herokuapp.com/	/auth/token/login/		User login
https://greeterycards.herokuapp.com/	/auth/users/reset_password/		Reset Password- Generates a reset email
https://greeterycards.herokuapp.com/	/ecard/create/		Creates a New Card
https://greeterycards.herokuapp.com/	/auth/token/logout/		User Log out
https://greeterycards.herokuapp.com/	/ecard/follow/<id>/	-	Unfollow or Follow [] Will Indicate User id
https://greeterycards.herokuapp.com/	ecard/favorited_by/<id>/		User Favorite or Unfavorite Cards