FROM python:3.9

RUN apt-get update
RUN pip install mkdocs Pygments pymdown-extensions lunr mkdocs-gitbook mkdocs-exclude-search
RUN pip install mkdocs-exclude mkdocs-enumerate-headings-plugin mkdocs-minify-plugin
RUN pip install mkdocs-redirects mkdocs-mermaid2-plugin
RUN pip install mkdocs-nav-enhancements mkdocs-simple-hooks mkdocs-section-index
RUN pip install mkdocs-git-revision-date-localized-plugin mkdocs-ezlinks-plugin markdown-svgbob
RUN curl -sSf https://sh.rustup.rs | sh -s -- -y
RUN echo 'source $HOME/.cargo/env' >> $HOME/.bashrc
ENV PATH="/root/.cargo/bin:${PATH}"
RUN cargo install svgbob_cli

COPY ./ /opt/MemoryViewer
WORKDIR /opt/MemoryViewer

#RUN git clone https://github.com/squidfunk/mkdocs-material
#WORKDIR /opt/MemoryViewer/mkdocs-material
#RUN python ./setup.py install

WORKDIR /opt/MemoryViewer

COPY ./custom_codefences.py /usr/local/lib/python3.9/site-packages/pymdownx/
RUN PYTHONPATH=/opt/MemoryViewer mkdocs build -v 

EXPOSE 8000
CMD ["python3", "-m", "http.server", "-d", "/opt/MemoryViewer/site", "8000"]
