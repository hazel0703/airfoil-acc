# airfoil-acc
This is the repository for the airfoil project

runme.sh: bash script controlling the execution of generating GMSH .msh mesh files
naca2gmsh_geo.py: python script generatimng GMSH .geo geometry files
geo folder: is a directory where geo files are going to be stored
msh folder: is a directory where msh files are going to be stored

What is needed:

Need to be installed GMSH:, go to http://geuz.org/gmsh/
Need to be installed sudo apt-get install dolfin-bin
edit the paths and variables in the runme.sh file
edit path to python in shebang of naca2gmsh_geo.py
run runme.sh with appropriate arguments (se runme.sh for example)
