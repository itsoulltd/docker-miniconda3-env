FROM continuumio/miniconda3

# Install gcc and other essential build systems.
RUN apt-get update \
    && apt-get install -y build-essential

# Update conda.
RUN conda update -n base -c defaults conda

# Create the environment:
COPY environment.yaml .
RUN conda env create -f environment.yaml

WORKDIR /home

ENTRYPOINT ["conda", "run", "-n", "myenv", "jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--allow-root", "--NotebookApp.token=''", "--NotebookApp.password=''"]

#End-Of-File