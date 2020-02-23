# Core of Science - Files

_This is pretty much construction all over the place_

The idea here is to have a somewhat performant authenticated file store.


## Running

_Again this is pretty much draft everywhere_

```console
docker-compose up --build
```

You need to manually add some files to the storage place, you can do that with

```console
docker-compose exec storage bash
echo "secret content" >> /usr/share/nginx/html/file.txt
exit
```

## Development

Check `files.py`.

## Testing

Write features and run them with [behave], make assertions with [grappa] for more debug info on errors.


[behave]: https://behave.readthedocs.io/en/latest/
[grappa]: https://grappa.readthedocs.io/en/latest/