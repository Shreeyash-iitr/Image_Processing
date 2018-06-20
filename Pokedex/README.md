<h3> Pokedex- identify the pokemon</h3>

I have given dataset for pokemon, and this program is a simple pokemon search engine which identify the pokemon in given image.
<img src="output.png">
first it segments the screen portion of pokedex(here <a href="https://bulbapedia.bulbagarden.net/wiki/Marowak_(Pok%C3%A9mon)"MAROWAK</a>) and then program crops out the image of pokemon in upper right corner.
I used ZernikeMoments as my shape descriptors. Euclidean distance has been used as distance matric to find similar pokemon from dataset.Program prints the name of pokemon as output.
