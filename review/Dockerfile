FROM registry.access.redhat.com/ubi8/ubi:latest

MAINTAINER andrew.campagna@ibm.com

LABEL io.openshift.expose-services="5000"

WORKDIR /api/review

RUN yum -y install python3 \
	&& yum clean all -y \
	&& pip3 install flask

COPY . .

RUN chgrp -R 0 /api/review /api/review \
	&& chmod -R g=u /api/review

EXPOSE 5000

USER 1001

CMD ["python3", "app.py"]