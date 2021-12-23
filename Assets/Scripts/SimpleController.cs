using UnityEngine;
using UnityEngine.InputSystem;

public class SimpleController : MonoBehaviour
{
    [SerializeField] Vector3 moveValue;
    [SerializeField] float moveSpeed;

    private bool ready = true;

    void OnGUI()
    {
        if (GUI.Button(new Rect(10, 10, 150, 100), "Lick me")) {
            Debug.Log("You licked the buttn!");
        }
    }

    // Start is called before the first frame update
    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {
        if (!ready)
        {
            ready = true;
        }
    }

    void FixedUpdate()
    {
        GameObject ship = GameObject.FindGameObjectWithTag("Player");
        ship.transform.position += moveSpeed * Time.deltaTime * moveValue;

        // var keyboard = Keyboard.current;

        // if (keyboard.wKey.isPressed) {
        //     ship.transform.position += new Vector3(1, 0, 0);
        // }

        // if (keyboard.sKey.isPressed) {
        //   ship.transform.position += new Vector3(-1, 0, 0);
        // }

        // var gamepad = Gamepad.current;
        // if (gamepad == null) {
        //     Debug.Log("No controller");
        //     return;
        // }

        // if (gamepad.rightTrigger.wasPressedThisFrame) {
        //     Debug.Log("pressing right trigger");
        // }

        // Vector2 move = gamepad.leftStick.ReadValue();
        // // move code here
    }

    void OnMove(InputValue value)
    {
        Vector2 normalized = value.Get<Vector2>().normalized;

        moveValue = new Vector3(normalized.y, 0, -normalized.x);
    }

    void OnLook(InputValue value)
    {
        GameObject ship = GameObject.FindGameObjectWithTag("Player");
        Vector2 look = value.Get<Vector2>();
        Debug.Log(look);

        float xRotation = -look.y * 100f * Time.deltaTime;
        xRotation = Mathf.Clamp(xRotation, -90f, 90f);

        ship.transform.localRotation = Quaternion.Euler(xRotation, 0f, 0f);
        ship.transform.Rotate(Vector3.up * look.x * 100f * Time.deltaTime);
    }

    void OnJump(InputValue value)
    {
        Debug.Log("Jumping!");
    }

    void OnFire(InputValue value)
    {
        if (ready)
        {
            ready = false;
            Debug.Log("Firing!");
        }
    }
}
