FROM gradle:6.5.1-jdk11 AS build

EXPOSE 8080

COPY --chown=gradle:gradle build.gradle /home/gradle/src/
COPY --chown=gradle:gradle settings.gradle /home/gradle/src/
COPY --chown=gradle:gradle gradle /home/gradle/src/
COPY --chown=gradle:gradle src /home/gradle/src/src

WORKDIR /home/gradle/src
RUN gradle build --no-daemon
RUN cp /home/gradle/src/build/libs/app.jar /app.jar

# # Old build container, only for deployments, not development
# FROM openjdk:8-jre-slim
#FROM gradle:6.5.1-jdk11
RUN mkdir /app
#COPY --from=build /app.jar /app.jar

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" "deployment" ]
