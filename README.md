# nanoml

A collection of **nano** utility functions to make the **ML** code cleaner

> [!IMPORTANT]
> This project is under active development. Feel free to open an issue or submit a pull request.

```bash
pip install nanoml
```

## Documentation

- [Documentation](https://nanoml.roydipta.com)

## Example

```python
from nanoml.dtype import is_bf16_supported

print(is_bf16_supported())
# True if bfloat16 is supported, False otherwise
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

### Contribution Steps:

1. Fork the repository
2. Create a new branch
3. Run `uv sync` or `pip install -e .` to install the dependencies
4. Run `pre-commit install` to install the pre-commit hooks
5. Make your changes and commit them
6. Push to your fork
7. Open a PR


## License

MIT
