# ElTwittoDelDiablo v1.0

![ElTwittoDelDiablo-logo](docs/pics/product-logo.png)

A bot that searches for exotic emoticons on the twitter platform

## Summary

1. [Docker Use](#docker-use)
	- [Application Container](#application-container)
	- [Grafana Container](#grafana-container)
2. [Application](#application)
3. [Grafana](#grafana)

Note: go to [Solution Relative aux Analyses](docs/solution_relative.md) if you want to see the exercice report

## Docker Use

Just type `~$ docker-compose up` to initiate all containers.

Note: run `~$ docker-compose restart eltwittodeldiablo-api` if api container fail on the first running.

[Summary](#summary)

### Application Container

Main python application is running on a docker container who requesting database connection on cloud and twitter api v2.

[Summary](#summary)

### Grafana Container

Grafana container is running after [Application Container](#application-container) and store all dashboard data on [grafana](grafana) folder where stored all information about users, dashboards, groups related to grafana interface.

[Summary](#summary)

## Application

Install all dependencies with `~$ pip install -r requirements.txt`.

[Summary](#summary)

## Grafana

Type `localhost:3000` on your browser to access to grafana interface and manage this, the login access is `admin:admin` & the **dashboard name is ElTwittoDelDiablo** in general.

[Summary](#summary)

## GraphQL Database