mkdir tempdir
mkdir tempdir/templates
mkdir tempdir/static

cp sample_app.py tempdir/.
cp -r templates/* tempdir/templates/.
cp -r static/* tempdir/static/.

echo "FROM python" > tempdir/Dockerfile
echo "RUN pip install flask" >> tempdir/Dockerfile
echo "COPY  ./static /home/ubuntu/static/" >> tempdir/Dockerfile
echo "COPY  ./templates /home/ubuntu/templates/" >> tempdir/Dockerfile
echo "COPY  sample_app.py /home/ubuntu/" >> tempdir/Dockerfile
echo "EXPOSE 80" >> tempdir/Dockerfile
echo "CMD python /home/ubuntu/sample_app.py" >> tempdir/Dockerfile

cd tempdir
sudo docker build -t sampleapp .

sudo docker stop samplerunning
sudo docker rm samplerunning
sudo docker run -t -d -p 8000:80 --name samplerunning sampleapp
sudo docker ps -a
