echo " BUILD START"
pytohn3.11 -m pip install -r requirements.txt
pytohn3.11 manage.py collectstatic --noinput --clear
echo " BUILD END"