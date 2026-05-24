import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import FormHelperText from '@mui/material/FormHelperText';
import Select, { SelectChangeEvent } from '@mui/material/Select';


interface SelectNumberRowProps {
  label: string
  selectionList: string[]
	value: number
	setValue: (value: number) => void
	addEmptyElement?: boolean 
  isInvalidRow?: boolean
  selectHandler?: () => void
}

export function SelectNumberRow(props: SelectNumberRowProps) {
  const handleChange = (event: SelectChangeEvent) => {
    props.setValue(Number(event.target.value));

    if (props.selectHandler) {
			props.selectHandler();
		}
  };

  return (
    <div>
      <FormControl 
        fullWidth 
        error={props.isInvalidRow}
      >
        <InputLabel id="simple-select-autowidth-label">{ props.label }</InputLabel>
        <Select
          labelId="simple-select-autowidth-label"
          id="simple-select-autowidth"
          value={ props.value !== -1 ? String(props.value) : "" }
          onChange={ handleChange }
          label={ props.label }
        >
          { props.addEmptyElement &&
            <MenuItem value={-1} key={-1}>
              <em>—</em>
            </MenuItem>
          }  
          { props.selectionList.map((item, index) =>
              <MenuItem value={ index } key={ index }>{ item }</MenuItem>
            )
          }
        </Select>
        {props.isInvalidRow &&
          <FormHelperText>Обязательное поле</FormHelperText>
        }
      </FormControl>
    </div>
  );
}
