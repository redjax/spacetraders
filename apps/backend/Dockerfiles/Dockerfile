## PDM in Docker:
#  https://pdm.fming.dev/latest/usage/advanced/#use-pdm-in-a-multi-stage-dockerfile
FROM python:3.10-slim as base

## Set Python env variables
ENV PYTHONUNBUFFERED=1 \
    # prevents python creating .pyc files
    PYTHONDONTWRITEBYTECODE=1 \
    \
    # pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

## Install CURL for healthcheck
RUN apt-get update -y && \
    apt-get install -y curl

## Install pdm
RUN pip install -U pip setuptools wheel
RUN pip install pdm

## Copy project files into container
COPY pyproject.toml pdm.lock /project/
COPY spacetraders /project/spacetraders

FROM base as build

COPY --from=base /project /project

WORKDIR /project
## Install dependencies
RUN mkdir __pypackages__ && pdm install --prod --no-lock --no-editable

FROM base as production

## Retrieve packages from build stage
ENV PYTHONPATH=/project/pkgs
COPY --from=build /project/__pypackages__/3.10/lib /project/pkgs
COPY --from=build /project /project

## Set entrypoint
EXPOSE 8000

WORKDIR /project

ENTRYPOINT ["pdm", "run", "start-server"]
