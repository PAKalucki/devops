FROM runmymind/docker-android-sdk:alpine-standalone

ENV CLOUD_SDK_VERSION 203.0.0
ENV PATH /opt/android-sdk-linux/google-cloud-sdk/bin:$PATH

ADD key.jks /opt/keystore/key.jks
ADD keystore.properties /opt/keystore/keystore.properties
ADD service_key.p12 /opt/keystore/service_key.p12

RUN apk --no-cache add \
        curl \
        python \
        py-crcmod \
        bash \
        openssh-client \
        git \
    && curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \
    tar xzf google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \
    rm google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \
    ln -s /lib /lib64 && \
    bash gcloud config set core/disable_usage_reporting true && \
    bash gcloud config set component_manager/disable_update_check true && \
    bash gcloud config set metrics/environment github_docker_image && \
    bash gcloud --version