import typer

from rf_visuals.handlers.s1p import visualize_s1p
from rf_visuals.handlers.s2p import visualize_s2p

app = typer.Typer(help="A tool to visualize S-parameter data.")


@app.command("s1p", help="Visualize data from an S1P file.")
def s1p_command(
    input_file: str = typer.Argument(
        None, help="Path to the S1P file. If not provided, data is read from stdin."
    ),
):
    typer.echo(visualize_s1p(input_file).__str__())


@app.command("s2p", help="Visualize data from an S2P file.")
def s2p_command(
    input_file: str = typer.Argument(
        None, help="Path to the S2P file. If not provided, data is read from stdin."
    ),
):
    typer.echo(visualize_s2p(input_file).__str__())


if __name__ == "__main__":
    app()
