cd apps

rm -f authors/migrations/*.py
touch authors/migrations/__init__.py

rm -f comments/migrations/*.py
touch comments/migrations/__init__.py

rm -f docs/migrations/*.py
touch docs/migrations/__init__.py

rm -f followers/migrations/*.py
touch followers/migrations/__init__.py

rm -f inbox/migrations/*.py
touch inbox/migrations/__init__.py

rm -f likes/migrations/*.py
touch likes/migrations/__init__.py

rm -f posts/migrations/*.py
touch posts/migrations/__init__.py
