FROM registry.access.redhat.com/ubi8/ubi-minimal
RUN microdnf install -y python3 python3-devel redhat-rpm-config gcc libffi-devel openssl-devel cargo 
WORKDIR /app
COPY src/requirements.txt /app/
RUN python3 -m pip install setuptools_rust
RUN python3 -m pip install -r /app/requirements.txt
COPY src/orders.py /app/
# Create and set user
USER 1000
EXPOSE 12345
ENV APP_FILE=/app/orders.py
CMD ["python3", "/app/orders.py"]
