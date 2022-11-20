from enc import recrypt_SEB
from dec import decrypt_SEB
from gooey import Gooey, GooeyParser


@Gooey(advanced=True, program_name="SEBroken", tabbed_groups=True, image_dir="./icons")
def main():
    parser = GooeyParser(prog="SEBroken", description="An SEB file patcher.")
    required_args = parser.add_argument_group("Required Arguments")
    opt_args = parser.add_argument_group("Optional Arguments")
    required_args.add_argument(
        "-f",
        "--filename",
        help="The SEB file to process\n(NOTE: OUTPUTS ARE IN THE SAME DIRECTORY AS THIS).",
        default="encrypted.seb",
        widget="FileChooser",
        required=True,
    )
    required_args.add_argument(
        "-p",
        "--password",
        help="The exam/encryption password.",
        default="password",
        required=True,
    )
    required_args.add_argument(
        "-ap",
        "--authpassword",
        help="New admin/quit password.",
        default="password",
        required=True,
    )
    opt_args.add_argument(
        "-np",
        "--newpassword",
        help="New exam/encryption password, defaults to the old one.",
        required=False,
    )
    args = parser.parse_args()
    decrypt_SEB(
        args.password,
        args.newpassword if args.newpassword else args.password,
        args.filename,
    )
    recrypt_SEB(
        args.newpassword if args.newpassword else args.password,
        f"{args.filename.split('.').pop(0)}.decrypted.seb",
        f"{args.filename.split('.').pop(0)}.patched.seb",
    )


if __name__ == "__main__":
    main()
