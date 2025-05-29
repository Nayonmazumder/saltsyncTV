import os

def generate_m3u8_entry(channel_name, stream_url, logo_url, tvg_id="custom-id", tvg_group="NEWS"):
    return (
        f'#EXTINF:-1 tvg-id="{tvg_id}" tvg-name="{channel_name}" tvg-logo="{logo_url}" group-title="{tvg_group}",{channel_name}\n'
        f"{stream_url}\n"
    )

def ensure_newline_before_append(filepath):
    """Ensures that the file ends with a newline before appending."""
    with open(filepath, "rb+") as f:
        f.seek(-1, os.SEEK_END)
        last_char = f.read(1)
        if last_char != b'\n':
            f.write(b'\n')

def main():
    output_file = "output.m3u8"
    file_exists = os.path.exists(output_file)

    if file_exists:
        ensure_newline_before_append(output_file)
        mode = "a"
    else:
        mode = "w"

    with open(output_file, mode) as f:
        print("Enter channel details (type 'done' as Channel Name to finish):\n")
        while True:
            channel_name = input("Channel Name: ")
            if channel_name.lower() == "done":
                break
            stream_url = input("Stream URL (.m3u8 or .ts): ")
            logo_url = input("Logo URL: ")
            tvg_id = input("TVG-ID (press enter for default): ") or "custom-id"
            group = input("Group Title (press enter for NEWS): ") or "NEWS"

            entry = generate_m3u8_entry(channel_name, stream_url, logo_url, tvg_id, group)
            f.write(entry)
            print(f"✅ Entry for '{channel_name}' added.\n")

    print(f"\n✅ All entries saved to: {output_file}")

if __name__ == "__main__":
    main()
