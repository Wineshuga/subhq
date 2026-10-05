FROM python:3.11.17-alpine3.23

WORKDIR /app

RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Download dependencies as a separate step to take advantage of Docker's caching.
# Leverage a cache mount to /root/.cache/pip to speed up subsequent builds.
# Leverage a bind mount to requirements.txt to avoid having to copy them into
# this layer.
RUN --mount=type=cache,target=/root/.cache/pip \
  --mount=type=bind,source=app/requirements.txt,target=requirements.txt \
  pip install -r requirements.txt

# Copy the source code into the container.
COPY app/ .

# Expose the port that the application listens on.
EXPOSE 8000

# Run the application.
CMD ["/venv/bin/python3", "-m", "uvicorn", "main:app", "--host=0.0.0.0", "--port=8000"]
