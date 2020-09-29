# phylogenic-tree

This is the back-end of the Phylogenic-Tree Viewing software for the Bioinformatics Reserach Group (BRG) at BYU.

The ideas of the back-end are drawn on the "db_overview.jpg". 

# current status (5/26/20)

As of 5/26/20, the back-end has not been completely implemented as some of the DAOs have not been finished or tested. However, there is code in python that interacts with the SQLite database.

One limitation with SQLite is that, no more than one person can edit or make changes to the database at the sametime. Because the purpose of this project is to create a minimum viable project (MVP), as a club we have decided to stick to SQLite for the time being as it is a database most club members are familar with. (In the future, I suggest that programmers should look into PostgresQL or any other powerful databases when creating a better verision of this project.)

Another note that programmers must understand is that, there is no server hosting our database. To test and run these scripts, coders must execute them on their own machines. (In the future, I suggest that the club should look into finding ways to host the database. For example, DigitalOcean would be a great place to host it but with a monthly subscription. If the club would like to find a place to host the database, I would probably ask BYU's Office of Research Computing if they can create a server for the club.)

# to do

From what I can see, the biggest thing that needs to be done next is finishing up the unfinished scripts and then testing each script throughly. When testing, I suggest finding a way to run all the scripts automatically with unit tests.

Other than that, once everything is done, the purpose of the back-end of the MVP should be done and members on the back-end team can join the front end.

# the project

Determining the relatedness of species is fundamental to understanding biology. Unfortunately, software packages for representing this relatedness in phylogenies do not have the features that an evolutionary biologist needs to easily visualize species relationships. Outdated visualization techniques with limited support for current phylogenetic formats limits the usefulness of current phylogenetic tree viewing software and makes creating a publication-ready tree difficult and time-consuming. Using a web-based programming language such as JavaScript, phylogenetic tree viewing software should have the following features:

1. Fully editable so that users can correct misspelled taxa on the tree
2. Easily color specific clades with one or more colors, including an optional legend
3. Able to add arrows (to point to regions) or other clip art to any part of the phylogeny
4. Easily add clade pictures from http://phylopic.org/
5. Variable and editable font sizes/ font type/ branch lengths
6. Collapsible clades so that large trees can be condensed
7. Support horizontal gene transfer with dashed lines
8. 3D drag (for web/app) for viewing horizontal gene transfer relationships better
9. Be able to copy the phylogeny without saving it
10. Save phylogeny as a JPEG, PNG, and SVG
11. Auto-format the smallest clades to the top of the phylogeny    
12. Support JSON format for reading and exporting. Also support legacy formats
13. Option to manually add/remove taxa
14. Option to align taxa to the far right
15. Option to make all edges equal sizes
16. Option to make edges square or rounded
17. Add bootstrap/ custom labels
18. Format phylogeny to fit on a single page.
a. Support tall and skinny phylogenies
b. Support short and fat phylogenies  
19. Option for circular phylogeny
20. Option for phylogeny/ clade titles
21. Option for a watermark


Authors:
Dane Jo
atambe123
rhadden2
Snicker7
