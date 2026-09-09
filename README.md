# boxes
A discord bot to hold your hyperlinks in an easy to use database.

## Bot Commands

### `/boxadd`

Appends an entry to an existing named box, or creates a new box if one does not already exist.

**Usage:**

```text
/boxadd <box-name> <entry-name> <hyperlink>
```

**Options:**

| Option | Description |
|---|---|
| `box-name` | Name of the box to add the entry to (Optional)|
| `entry-name` | Name of the new entry (Optional)|
| `hyperlink` | URL associated with the entry |

---

### `/boxdel`

Deletes a box, a specific entry, a list of entries, or all entries matching the provided options.

**Usage:**

```text
/boxdel <box-name> [entry-name (OR) entry-index (OR) entry-index-range]
```

**Options:**

| Option | Description |
|---|---|
| `box-name` | Name of the box |
| `entry-name` | Name of the entry to delete |
| `entry-index` | Index of the entry to delete |
| `entry-index-range` | Range of entry indexes to delete |

---

### `/box`

Returns the contents of a box or displays a specific entry.

**Usage:**

```text
/box <box-name> [entry-name (OR) entry-index]
```

**Options:**

| Option | Description |
|---|---|
| `box-name` | Name of the box to view |
| `entry-name` | Name of a specific entry to display |
| `entry-index` | Index of a specific entry to display |

---

### `/boxes`

Searches boxes for a specific entry or a list of entries.

**Usage:**

```text
/boxes [flag] [keyword]
```

**Options:**

| Option | Description |
|---|---|
| `flag` | Controls how the search is performed |
| `keyword` | Keyword to search for |
```
